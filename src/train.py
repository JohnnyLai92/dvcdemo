from dvclive import Live
with Live(save_dvc_exp=True) as live:
  # 讀取檔案
  with open('data\dvcdemo.txt', 'r') as file:
    numbers = file.readlines()
  for epoch in numbers:
    live.log_metric("accuracy", epoch)
    live.log_metric("loss", epoch)
    live.next_step()