{
  description = "rotation-station dev shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.11";
  };

  outputs =
    { nixpkgs, ... }:
    let
      pkgs = nixpkgs.legacyPackages."x86_64-linux";
    in
    {
      devShells."x86_64-linux".default = pkgs.mkShell {

        packages = [
          pkgs.python312

          # imports
          pkgs.python312Packages.matplotlib
        ];

        shellHook = ''
          # zellij --layout ./zj-rot.kdl
          # exit
        '';
      };
    };
}
