import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        try {
            File file = new File("src/random1.txt");
            Scanner scanner = new Scanner (file);
            while (scanner.hasNextLine()) {
                String numbers = scanner.nextLine();
                int k = 15;
                int t = 20;
                String text = scanner.nextLine();

                String[] sequences = new String[t];
                String sequence = "";

                int index = 0;
                for (int i = 0; i < text.length(); i++) {
                    if (text.charAt(i) != ' ' && i != text.length() - 1) {
                        sequence += text.charAt(i);
                    }
                    else {
                        sequences[index] = sequence;
                        index++;
                        sequence = "";
                    }
                }

                RandomSearch rSearch = new RandomSearch(k, t, sequences);
                int min = k * t;
                String[] best = new String[]{};
                for (int i = 0; i < 1000; i++) {
                    String[] motifs = rSearch.search();
                    int score = rSearch.score(motifs);
                    if (score < min) {
                        min = score;
                        best = motifs;
                    }
                }

                for (int i = 0; i < best.length; i++) {
                    System.out.println(best[i]);
                }
                System.out.println(rSearch.score(best));
            }

        } catch(FileNotFoundException f) {
            System.out.println("file not found");
        }
    }
}
