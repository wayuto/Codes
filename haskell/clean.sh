find . -type f -exec file {} \; | grep ELF | cut -d: -f1 | xargs rm -f
rm -rf *.hi
