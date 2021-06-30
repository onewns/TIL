function solution(s) {

  // 압축이 불가능한 경우가 답중에 가장 최댓값
  let answer = s.length;


  // pattern의 길이별로 자르기 위한 for문
  for (let patternLength = 1; patternLength <= s.length / 2; patternLength++) {

    // pattern들을 만들어서 차례대로 저장
    const patterns = [];
    let pattern = '';
    for (let i = 0; i < s.length; i++) {
      pattern += s[i];
      if (pattern.length === patternLength) {
        patterns.push(pattern);
        pattern = '';
      }
    }

    // 마지막에 남는 부분을 처리하기 위함
    if (pattern) patterns.push(pattern)


    // 현재 패턴길이에 따른 실시간 길이 = temp
    let temp = 0;

    // 현재 패턴 및 반복횟수
    let currentPattern = patterns[0];
    let currentNum = 1;

    // 현재 패턴과 다음 패턴을 비교
    for (let i = 1; i < patterns.length; i++) {
      if (currentPattern === patterns[i]) {
        currentNum += 1;
      } else {
        if (currentNum > 1) {
          temp += String(currentNum).length;
          temp += currentPattern.length;
        }
        if (temp >= answer) break;
        currentPattern = patterns[i];
        currentNum = 1;
      }
    }
    if (currentNum > 1) temp += String(currentNum).length;
    temp += currentPattern.length;
    answer = Math.min(answer, temp)
  }
  return answer;
}