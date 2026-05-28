Requirements: Linux or Windows with WSL, and Docker.

Prepare the dataset.

```sh
docker compose --progress quiet run --rm srs-benchmark python -m src.main.prepare --processes 10
```

If you encounter issues on WSL when preparing the dataset such as `concurrent.futures.process.BrokenProcessPool`, try one of:

- Increase the memory limit with `.wslconfig`: https://learn.microsoft.com/windows/wsl/wsl-config
- Use a lower `--processes` number.

Run training and evaluation.

```sh
docker compose --progress quiet run --rm srs-benchmark bash src/main/run.sh
```
