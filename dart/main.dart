import 'dart:io';
import 'isPrime.dart';

void main() {
  int n = int.parse(stdin.readLineSync() ?? "0");
  print(isPrime(n) ? "$n is a prime number." : "$n is not a prime number.");
  main();
}
