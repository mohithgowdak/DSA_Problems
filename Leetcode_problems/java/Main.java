package java;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Example input:
        // 5
        // 1 2 3 4 5
        // 6
        // 3 4 5 6 7 8

        // Read the size and elements of the first list
        System.out.println("Enter the size of the first list:");
        int n = scanner.nextInt();
        System.out.println("Enter the size of the second list:");
        int m = scanner.nextInt();
        System.out.println("Enter the elements of the first list:");
        List<Integer> A = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            A.add(scanner.nextInt());
        }

        // Read the size and elements of the second list
        
        System.out.println("Enter the elements of the second list:");
        List<Integer> x = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            x.add(scanner.nextInt());
        }

        // Sort the second list
        Collections.sort(x);

        // Find common elements using binary search
        List<Integer> ans = new ArrayList<>();
        for (int element : A) {
            if (binarySearch(x, element)) {
                ans.add(element);
            }
        }

        // Print the result
        System.out.println("Common elements:");
        for (int it : ans) {
            System.out.print(it + " ");
        }
        System.out.println();
    }

    public static boolean binarySearch(List<Integer> arr, int target) {
        int left = 0, right = arr.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr.get(mid) == target) {
                return true;
            } else if (arr.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
