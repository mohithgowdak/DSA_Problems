import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class ReverseDiagonalSum {
    
    public static List<Integer> revdiag(int[][] mat, int srow, int scol) {
        List<Integer> delements = new ArrayList<>();
        int r = srow, c = scol;
        while (r < mat.length && c >= 0) {
            delements.add(mat[r][c]);
            r++;
            c--;
        }
        return delements;
    }

    public static void maxdiagsum(int[][] mat) {
        int M = mat.length;
        int N = mat[0].length;

        // Variables to track the maximum sum and corresponding diagonal
        int maxSum = Integer.MIN_VALUE;
        List<Integer> maxDiag = new ArrayList<>();

        // Check diagonals starting from each column of the first row
        for (int scol = 0; scol < N; scol++) {
            List<Integer> diag = revdiag(mat, 0, scol);
            int dsum = diag.stream().mapToInt(Integer::intValue).sum();
            if (dsum > maxSum) {
                maxSum = dsum;
                maxDiag = diag;
            }
        }

        // Check diagonals starting from each row of the last column
        for (int srow = 1; srow < M; srow++) {
            List<Integer> diag = revdiag(mat, srow, N - 1);
            int dsum = diag.stream().mapToInt(Integer::intValue).sum();
            if (dsum > maxSum) {
                maxSum = dsum;
                maxDiag = diag;
            }
        }

        // Output the results
        System.out.println(maxSum);
        Collections.sort(maxDiag, Collections.reverseOrder());
        for (int num : maxDiag) {
            System.out.print(num + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read mat dimensions
        int M = sc.nextInt();
        int N = sc.nextInt();
        
        // Read mat
        int[][] mat = new int[M][N];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                mat[i][j] = sc.nextInt();
            }
        }

        maxdiagsum(mat);
    }
}
