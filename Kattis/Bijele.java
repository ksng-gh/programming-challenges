import java.util.Scanner;

public class Bijele {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        final int KINGS = 1;
        final int QUEENS = 1;
        final int ROOKS = 2;
        final int BISHOPS = 2;
        final int KNIGHTS = 2;
        final int PAWNS = 8;

        int king = input.nextInt();
        int queen = input.nextInt();
        int rook = input.nextInt();
        int bishop = input.nextInt();
        int knight = input.nextInt();
        int pawn = input.nextInt();

        int k = KINGS - king;
        int q = QUEENS - queen;
        int r = ROOKS - rook;
        int b = BISHOPS - bishop;
        int n = KNIGHTS - knight;
        int p = PAWNS - pawn;

        System.out.print(k + " " + q + " " + r + " " + b + " " + n + " " + p);
        input.close();
    }
}
