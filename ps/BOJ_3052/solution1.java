package ps.BOJ_3052;

/**
 * solution1
 * Hashset 찾아봅시다
 */


import java.io.*;


public class solution1 {
  
  public static void main(String[] args) throws IOException {
    System.setIn(new FileInputStream("ps/input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num, answer;
    int[] visited = new int[42];
    answer = 0;
    for (int i = 0; i < 10; i++) {
      num = Integer.parseInt(br.readLine()) % 42;
      if (visited[num] == 0) {
        visited[num]++;
        answer++;
      }
    }
    System.out.println(answer);
  }
}