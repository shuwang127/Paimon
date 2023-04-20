from args import get_args
from src.train import Data_Prep, Train, Test

if __name__ == '__main__':
    opt = get_args()
    print(opt)

    if opt.task == 'train':
        if not opt.train_only:
            Data_Prep(opt)
        Train(opt)
    elif opt.task == 'test':
        Data_Prep(opt)
        Test(opt)
