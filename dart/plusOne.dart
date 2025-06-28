List<int> plusOne(List<int> digits) {
  int len = digits.length;
  for (int i = 0; i < len; i++) {
    if (digits[len - 1 - i] < 9) {
      digits[len - 1 - i]++;
      return digits;
    } else {
      digits[len - 1 - i] = 0;
    }
  }
  digits.insert(0, 1);
  return digits;
}
