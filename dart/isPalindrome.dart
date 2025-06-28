bool isPalindrome(String s) {
  String newS = s.toLowerCase().replaceAll(RegExp(r"[^a-z0-9]+"), "");
  print(newS);
  for (int i = 0; i < newS.length ~/ 2; i++) {
    if (newS[i] != newS[newS.length - 1 - i]) {
      return false;
    }
  }
  return true;
}
