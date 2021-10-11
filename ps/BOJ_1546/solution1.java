package ps.BOJ_1546;

/**
 * solution1
 */

import java.io.*;
import java.util.*;

public class solution1 {
  public static void main(String[] args) throws IOException {
    System.setIn(new FileInputStream("ps/input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    double n, max, sum, score, answer;
    StringTokenizer st;
    n = Integer.parseInt(br.readLine());
    sum = 0;
    max = 0;
    st = new StringTokenizer(br.readLine(), " ");
    while (st.hasMoreTokens()) {
      score = Integer.parseInt(st.nextToken());
      if (max < score) {
        max = score;
      };
      sum += score;
    }
    answer = (sum / max) * 100 / n;
    System.out.println(answer);
  }
}