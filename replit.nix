{ pkgs }: {
  deps = [
    pkgs.python311Packages.ipython
    pkgs.python310Packages.pytest
    pkgs.python311Packages.pytest
  ];
}