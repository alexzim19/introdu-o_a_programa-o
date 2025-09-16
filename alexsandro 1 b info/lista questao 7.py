thanos = 1.50
homenAranha = 1.10
anos = 0
for i in range(100):
    thanos=thanos+0.02
    homenAranha=homenAranha+0.03
    anos=anos+1
    if homenAranha>thanos:
        break
print(anos)
        