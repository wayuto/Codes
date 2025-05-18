from syntax import cpp

@cpp
def main(cout, endl, cin) -> None:
    i = None
    i = cin >> i;
    cout << type(i) << " " << i << endl;

if __name__ == "__main__":
    main()