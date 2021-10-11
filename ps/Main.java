package ps;

// import java.io.BufferedReader;
// // import java.io.FileInputStream;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.StringTokenizer;

// /**
//  * Main
//  */
// public class Main {

//   public static void main(String[] args) throws IOException {
//     // System.setIn(new FileInputStream("ps/input.txt"));
//     int a, b;
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//     a = Integer.parseInt(st.nextToken());
//     b = Integer.parseInt(st.nextToken());
//     System.out.println(a + b);
//     System.out.println(a - b);
//     System.out.println(a / b);
//     System.out.println(a % b);
//   }
// }

// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int a = Integer.parseInt(br.readLine());
//     String b = br.readLine();
//     for (int i = 2; i >= 0; i--) {
//       System.out.println(a * (b.charAt(i) - '0'));
//     }

//     System.out.println(a * Integer.parseInt(b));
//   }
// }

// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//     int a, b;
//     a = Integer.parseInt(st.nextToken());
//     b = Integer.parseInt(st.nextToken());
//     if (a > b) {
//       System.out.println('>');
//     } else if ( a < b) {
//       System.out.println('<');
//     } else {
//       System.out.println("==");
//     }
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int score = Integer.parseInt(br.readLine());
//     if (score >= 90) {
//       System.out.println('A');
//     } else if (score >= 80) {
//       System.out.println('B');
//     } else if (score >= 70) {
//       System.out.println('C');
//     } else if (score >= 60) {
//       System.out.println('D');
//     } else {
//       System.out.println('F');
//     }
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int year = Integer.parseInt(br.readLine());
//     if (year % 400 == 0) {
//       System.out.println(1);
//     } else if (year % 100 == 0) {
//       System.out.println(0);
//     } else if (year % 4 == 0) {
//       System.out.println(1);
//     } else {
//       System.out.println(0);
//     }
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     int x, y;
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     x = Integer.parseInt(br.readLine());
//     y = Integer.parseInt(br.readLine());
//     if (x > 0) {
//       if (y > 0) {
//         System.out.println(1);
//       } else {
//         System.out.println(4);
//       }
//     } else {
//       if (y > 0) {
//         System.out.println(2);
//       } else {
//         System.out.println(3);
//       }
//     }
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     int hour, minute;
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//     hour =  Integer.parseInt(st.nextToken());
//     minute = Integer.parseInt(st.nextToken());
//     if (minute >= 45) {
//       System.out.printf("%d %d", hour, minute-45);
//     } else {
//       if (hour == 0) {
//         System.out.printf("%d %d", 23, minute+15);
//       } else {
//         System.out.printf("%d %d", hour-1, minute+15);
//       }
//     }
//   }
// }

// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int n = Integer.parseInt(br.readLine());
//     for (int i = 1; i < 10; i++) {
//       System.out.printf("%d * %d = %d\n", n, i, n*i);
//     }
//   }
// }

// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int tc = Integer.parseInt(br.readLine());
//     for (int i = 0; i < tc; i++) {
//       StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//       int a = Integer.parseInt(st.nextToken());
//       int b = Integer.parseInt(st.nextToken());
//       System.out.println(a + b);
//     }
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int n = Integer.parseInt(br.readLine());
//     System.out.printf("%d", n * (n + 1) / 2);
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int tc = Integer.parseInt(br.readLine());
//     for (int i = 0; i < tc; i++) {
//       StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//       int a, b;
//       a = Integer.parseInt(st.nextToken());
//       b = Integer.parseInt(st.nextToken());
//       bw.write((a+b)+"\n");
//     }
//     bw.flush();
//   }
// }

// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int n = Integer.parseInt(br.readLine());
//     for (int i = 1; i < n + 1; i++) {
//       bw.write(i+"\n");
//     }
//     bw.flush();
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int n = Integer.parseInt(br.readLine());
//     for (int i = n; i > 0; i--) {
//       bw.write(i+"\n");
//     }
//     bw.flush();
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int t = Integer.parseInt(br.readLine());
//     int a;
//     StringTokenizer st;
//     for (int tc = 1; tc <= t; tc++) {
//       st = new StringTokenizer(br.readLine());
//       a = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
//       bw.write("Case #"+tc+": "+a+"\n");
//     }
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int t = Integer.parseInt(br.readLine());
//     int a, b;
//     StringTokenizer st;
//     for (int tc = 1; tc <= t; tc++) {
//       st = new StringTokenizer(br.readLine());
//       a = Integer.parseInt(st.nextToken());
//       b = Integer.parseInt(st.nextToken());
//       bw.write("Case #"+tc+": "+a+" + "+b+" = "+(a+b)+"\n");
//     }
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int n = Integer.parseInt(br.readLine());
//     for (int i = 0; i < n; i++) {
//       for (int j = 0; j < i+1; j++) {
//         bw.write("*");
//       }
//       bw.write("\n");
//     }
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     int n = Integer.parseInt(br.readLine());
//     for (int i = 0; i < n; i++) {
//       String temp = "";
//       for (int j = 0; j < i+1; j++) {
//         temp = temp + "*";
//       }
//       bw.write(String.format("%"+n+"s\n", temp));
//     }
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//     int N, X, temp;
//     N = Integer.parseInt(st.nextToken());
//     X = Integer.parseInt(st.nextToken());
//     st = new StringTokenizer(br.readLine(), " ");
//     while (st.hasMoreTokens()) {
//       temp = Integer.parseInt(st.nextToken());
//       if (temp < X) {
//         bw.write(temp+" ");
//       }
//     }
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     StringTokenizer st;
//     int a, b;
//     while (true) {
//       st = new StringTokenizer(br.readLine(), " ");
//       a = Integer.parseInt(st.nextToken());
//       b = Integer.parseInt(st.nextToken());
//       if (a == 0 && b == 0) {
//         break;
//       }
//       bw.write(String.format("%d\n", a+b));
//     };
//     bw.flush();
//     bw.close();
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//     StringTokenizer st;
//     String str;
//     int a, b;
//     while ((str = br.readLine()) != null) {
//       st = new StringTokenizer(str, " ");
//       a = Integer.parseInt(st.nextToken());
//       b = Integer.parseInt(st.nextToken());
//       bw.write(String.format("%d\n", a+b));
//     };
//     bw.flush();
//     bw.close();
//   }
// }

// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int n, number;
//     int answer = 0;
//     n = Integer.parseInt(br.readLine());
//     number = n;
//     do {
//       answer++;
//       number = number % 10 * 10 + (number/10 + number%10) % 10;
//     } while (n != number);
//     System.out.println(answer);
//   }
// }


// import java.io.*;
// import java.util.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int N = Integer.parseInt(br.readLine());
//     int max = -1000001, min = 1000001;
//     int temp;
//     StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//     for (int i = 0; i < N; i++) {
//       temp = Integer.parseInt(st.nextToken());
//       if (max < temp) {
//         max = temp;
//       }
//       if (min > temp) {
//         min = temp;
//       }
//     }
//     System.out.printf("%d %d", min, max);
//   }
// }

// import java.io.*;

// public class Main {
//   public static void main(String[] args) throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     int max, maxIndex, num;
//     max = 0;
//     maxIndex = 0;
//     for (int i = 0; i < 9; i++) {
//       num = Integer.parseInt(br.readLine());
//       if (num > max) {
//         max = num;
//         maxIndex = i + 1;
//       }
//     }
//     System.out.printf("%d\n%d", max, maxIndex);
//   }
// }


import java.io.*;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  public static void main(String[] args) throws IOException {
    int a, b, c, num;
    int[] counts = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    a = Integer.parseInt(br.readLine());
    b = Integer.parseInt(br.readLine());
    c = Integer.parseInt(br.readLine());
    num = a * b * c;
    String[] temp = String.valueOf(num).split("");
    for (int i = 0; i < temp.length; i++) {
      counts[Integer.parseInt(temp[i])]++;
    }
    for (int i = 0; i < counts.length; i++) {
      System.out.println(counts[i]);
    }
  }
}
