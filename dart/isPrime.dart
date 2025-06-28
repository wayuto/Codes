bool Function(int) isPrime = (int n) =>
    !RegExp(r"^1?$|^(11+?)\1+$").hasMatch("1" * n);
