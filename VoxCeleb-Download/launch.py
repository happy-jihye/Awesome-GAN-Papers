import os
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download youtube videos')

    parser.add_argument('-p', '--path',default="", type =str, help="directory path of voxceleb txt file")
    parser.add_argument('-d', '--docker_num', default=1, type=int, help="If you want to set up multiple dockers and download data fastly, put docker_num.")
    parser.add_argument('--error_txt_dir', default='vox2_frame', type=int, help="Directory containing the error txt file that was created when the python file was first run")
    parser.add_argument('--port', default=50000, type=int)

    args = parser.parse_args()

    port = args.port

    # 1. Download data through the voxceleb folder path
    if args.path != "":
        id_list = [file for file in os.listdir(args.path) if os.path.isdir(args.path) ]
        id_num_per_doc = int(len(id_list)/args.docker_num)

        for doc in range (0, int(args.docker_num)):

            if doc != int(args.docker_num)-1:

                id_string = ""
                for num in range(id_num_per_doc):
                    id_string += id_list[doc*id_num_per_doc + num] + " " 
    
                os.system('docker run -d --rm -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_path /datasets/vox2_txt --id {5}'.format(port, port+1, port+2, doc, doc, id_string))
                print('docker run -it -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_path /datasets/vox2_txt'.format(port, port+1, port+2, doc, doc))
        else:

                id_string = ""
                for num in range(len(id_list[id_num_per_doc*doc : ])):
                    id_string += id_list[doc*id_num_per_doc + num] + " " 

                os.system('docker run -d --rm -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_path /datasets/vox2_txt --id {5}'.format(port, port+1, port+2, doc, doc, id_string))
                print('docker run -it -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_path /datasets/vox2_txt'.format(port, port+1, port+2, doc, doc))

        port = port + 3 
    
    # 2. Download data by error message
    else:
        err_file = []

        for i in range(3):
            f = open("{0}/error{1}.txt".format(args.error_txt_dir, i), 'r')
            data = f.read().split('\n')
            err_file = data + err_file
            print('total id', len(err_file))

        len_file = int(len(err_file)/args.docker_num)
        print('id per docker', len_file)


        for doc in range (0, int(args.docker_num)):
            if doc != int(args.docker_num)-1:

                id_file_string = ""
                for num in range(len_file):
                    id_file_string += err_file[doc*len_file + num] + " "

                os.system('docker run -d -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_file {5}'.format(port, port+1, port+2, doc, doc, id_file_string))

            else:
                id_file_string = ""
                for num in range(len(err_file[doc*len_file : ])):
                    id_file_string += err_file[doc*len_file + num] + " "

                os.system('docker run -d -p {0}:22 -p {1}:6006 -p {2}:8888 -v /home1/irteamsu/datasets:/datasets --name vox2_{3} --entrypoint="" jihye_pytorch_vox:0722 python3 /datasets/vox2_data.py --download_video --video_dir /datasets/vox2_frame --rank {4} --id_file {5}'.format(port, port+1, port+2, doc, doc, id_file_string))
            port = port + 3

