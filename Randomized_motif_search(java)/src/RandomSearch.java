import java.util.Arrays;
import java.util.HashMap;

public class RandomSearch {
    private int k;
    private int t;
    private String[] sequences;
    private HashMap<Character, Integer> indexes;

    /**
     * Creates a RandomSearch object that can do the random motif search
     * @param k the goal length of a kmer
     * @param t how many strands there are
     * @param sequences the given sequences of DNA
     */
    public RandomSearch(int k, int t, String[] sequences) {
        this.k = k;
        this.t = t;
        this.sequences = sequences;
        indexes = new HashMap<>();
        indexes.put('A', 0);
        indexes.put('C', 1);
        indexes.put('G', 2);
        indexes.put('T', 3);
    }

    /**
     * Performs a random motif search to find a kmer from each sequence
     * that minimizes the score
     * @return an array of kmers
     */
    public String[] search() {

        // first pick a random group of kmers
        String[] kmers = new String[t];
        int len = sequences[0].length();
        String[] best = new String[t];
        int minScore = k * t;
        for (int i = 0; i < sequences.length; i++) {
            int index = (int) ((len - k) * Math.random());
            kmers[i] = sequences[i].substring(index, index + k);
        }

        double[][] count;
        double[][] prof;

        int score = score(kmers);
        String[] previous = new String[] {};

        // run it until score stops improving
        while (score < minScore) {
            previous = kmers;
            minScore = score(previous);
            count = createCount(kmers);
            prof = createProfile(count);
            kmers = profileMostLikely(sequences, prof);
            score = score(kmers);
        }
        return previous;
    }

    /**
     * Creates a count matrix given the kmers. uses pseudocounts.
     * @param motifs is the motif matrix of kmers
     * @return a 2d array count matrix
     */
    private double[][] createCount(String[] motifs) {
        double[][] output = new double[4][k];

        for (int i = 0; i < motifs.length; i++) {
            String sequence = motifs[i];
            for (int j = 0; j < sequence.length(); j++) {
                char letter = sequence.charAt(j);
                int row = indexes.get(letter);
                output[row][j]++;
            }
        }

        // add 1 to each for pseudocounts
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                output[i][j]++;
            }
        }
        return output;
    }

    /**
     * Creates a profile matrix by dividing each entry by the column total
     * @param counts the count matrix
     * @return a 2d array profile matrix
     */
    private double[][] createProfile(double[][] counts) {
        double[][] output = counts;
        int total = t + 4;

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < k; j++) {
                output[i][j] /= total;
            }
        }
        return output;
    }

    /**
     * Finds the most likely k-mers given the sequences and a profile matrix
     * @param sequences the sequences of DNA given
     * @param profile the profile matrix created
     * @return a list of Strings containing the most likely k-mers
     */
    private String[] profileMostLikely(String[] sequences, double[][] profile) {
        String[] mostLikely = new String[t];

        for (int i = 0; i < sequences.length; i++) {
            String strand = sequences[i];
            HashMap<String, Double> freq = new HashMap<>();

            // iterate through all the kmers in each strand and calculate probabilities
            for (int j = 0; j < strand.length() - k + 1; j++) {
                String kmer = strand.substring(j, j + k);

                double product = 1;
                for (int n = 0; n < kmer.length(); n++) {
                    char letter = kmer.charAt(n);
                    product *= profile[indexes.get(letter)][n];
                }
                freq.put(kmer, product);
            }

            double max = 0;
            String bestKmer = "";
            // iterate through the HashMap to see which kmer has highest probability
            for (String key: freq.keySet()) {
                if (freq.get(key) > max) {
                    max = freq.get(key);
                    bestKmer = key;
                }
            }
            mostLikely[i] = bestKmer;
        }
        return mostLikely;
    }

    /**
     * Returns the score, or the number of mismatches from the median string
     * @param motifs 2d array with kmers
     * @return score
     */
    public int score(String[] motifs) {
        int score = 0;
        for (int i = 0; i < motifs[0].length(); i++) {

            HashMap<Character, Integer> counts = new HashMap<>();
            counts.put('A', 0);
            counts.put('C', 0);
            counts.put('G', 0);
            counts.put('T', 0);

            // iterate through every ith index in the strings, update the hashmap
            for (int m = 0; m < motifs.length; m++) {
                char letter = motifs[m].charAt(i);
                counts.put(letter, counts.get(letter) + 1);
            }

            // find the most common character for that index
            int max = 0;
            char common = 'A'; // random value
            for (Character key: counts.keySet()) {
                if (counts.get(key) > max) {
                    max = counts.get(key);
                    common = key;
                }
            }

            // add how many letters are not equal to that letter
            score += t - counts.get(common);
        }
        return score;
    }
}
