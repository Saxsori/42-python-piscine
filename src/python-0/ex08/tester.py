from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
#     print()
# print(tqdm(range(3)))
# for elem in ft_tqdm(range(333)):
#     sleep(0.5)
    # print()
for elem in ft_tqdm(range(333)):
    sleep(0.5)

# print(ft_tqdm(range(333)))
print('     ', end='')
print('█' * 180)