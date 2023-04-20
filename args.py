import argparse
import os

def check_dirs(dirs):
    dirs = [dirs] if type(dirs) not in [list, tuple] else dirs
    for d in dirs:
        try:
            os.makedirs(d)
        except OSError:
            pass
    return

def get_args():
    parser = argparse.ArgumentParser()

    ## Common Parameters ##
    parser.add_argument('-T', '--task', help='train | test', default='test', choices=['train', 'test'])

    ## Path Parameters ##
    parser.add_argument('--root', type=str, default='')
    # files paths
    parser.add_argument('--patch_path', type=str, default='_files/patches/')
    parser.add_argument('--repo_path', type=str, default='_files/repos/')
    parser.add_argument('--ab_path', type=str, default='_files/ab_files/')
    # dataset paths.
    parser.add_argument('--pdb_path', type=str, default='PatchDB/')
    parser.add_argument('--glog_path', type=str, default='_GraphLogs/')
    # data paths.
    parser.add_argument('--raw_path', type=str, default='_data/data_raw/')
    parser.add_argument('--mid_path', type=str, default='_data/data_mid/') #
    parser.add_argument('--np_path', type=str, default='_data/data_np/') #
    parser.add_argument('--np2_path', type=str, default='_data/data_np2/') #
    # testdata paths.
    parser.add_argument('--tmid_path', type=str, default='_testdata/data_mid/') #
    parser.add_argument('--tnp_path', type=str, default='_testdata/data_np/') #
    parser.add_argument('--tnp2_path', type=str, default='_testdata/data_np2/') #
    # logs paths.
    parser.add_argument('--log_path', type=str, default='logs/')
    parser.add_argument('--model_path', type=str, default='models/')
    # training file.
    parser.add_argument('--train_file', type=str, default='configs/patchdb.txt') #
    parser.add_argument('--test_file', type=str, default='configs/test.txt') #

    ## Parse parameters.
    parser.add_argument('--slicing', type=int, default=1)
    parser.add_argument('--twin_data', type=bool, default=True, action=argparse.BooleanOptionalAction)
    
    ## Embedding parameters.
    parser.add_argument('--embed_config', type=int, default=0)
    parser.add_argument('--conf_path', type=str, default="configs/")
    parser.add_argument('--embed_dim', type=int, default=768)
    parser.add_argument('--tokenizer')
    parser.add_argument('--embed_model')

    ## Optimizers Parameters ##
    parser.add_argument('--net', type=str, default='PGCN')
    parser.add_argument('--twin', type=bool, default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--train_rate', type=float, default=0.8)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=0.0001)
    parser.add_argument('--max_epoch', type=int, default=5000)
    parser.add_argument('--win_size', type=int, default=0)
    parser.add_argument('--first_epoch', type=int, default=0)
    parser.add_argument('--use_model',  type=bool, default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--train_only', type=bool, default=False, action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    check_dirs([args.mid_path, args.np_path, args.np2_path, 
                args.tmid_path, args.tnp_path, args.tnp2_path,
                args.log_path, args.model_path])
    
    return args