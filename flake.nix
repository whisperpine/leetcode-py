{
  description = "A Nix-flake-based Python development environment";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  outputs =
    inputs:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forEachSupportedSystem =
        f:
        inputs.nixpkgs.lib.genAttrs supportedSystems (
          system: f { pkgs = import inputs.nixpkgs { inherit system; }; }
        );
    in
    {
      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python313
              uv # python package and project manager
              just # just a command runner
              husky # managing git hooks
              typos # check misspelling
            ];
            shellHook = ''
              # install python project dependencies
              uv sync
              # active python virtual environment
              source .venv/bin/activate
              # install git hook managed by husky
              if [ ! -e "./.husky/_" ]; then
                husky install
              fi
            '';
          };
        }
      );
    };
}
