import os, argparse, cv2, glob

# download single youtube video
def download_single_youtube(id, rank, path = 'mp4', pytube_flag = True):

    youtubenum = id.split(os.sep)[-1]
    url = f'https://www.youtube.com/watch?v={youtubenum}'

    try :
        if pytube_flag :

            import pytube
            video = pytube.YouTube(url)
            #video.streams.all()
            video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(path)
        
        else: 
            import pafy

            video = pafy.new(url)
            best = video.getbest(preftype='mp4')
        
            print(os.path.join(path, youtubenum + '.mp4'))
            best.download(filepath=(os.path.join(path, youtubenum + '.mp4')))
    except:
        # write to error log
        with open(f'/datasets/vox2_frame/error{rank}.txt', 'a') as f:
           f.write(f'{id}\n')
        print(f'error downloading {id}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Download Youtube Video")

    parser.add_argument("--download_video", action='store_true', help="1. Download all youtube video in id")
    parser.add_argument("--video_to_frame", action='store_true', help="2. Extract Frame Images from all Videos")
    parser.add_argument("--frame_by_txt", action='store_true', help="3. Extract Specific Frame Images by Text File")
    parser.add_argument("--video_dir", type=str, default = 'video', help="directory to store video")
    parser.add_argument("--id_path", type=str, default = "", help="id (ex. Vox2/txt)")
    parser.add_argument("--id", nargs="+", type=str, default = "", help="id (ex. id10001 id10002 id10003)")
    parser.add_argument("--id_file", nargs="+", type=str, default = "", help="id and file (ex. id10001/kienfi2kd id10002/ekwifjd id10003/eiwkfod)")
    parser.add_argument("--pytube", default=True, help="download youtube video by pytube")
    parser.add_argument("--rank", type=int, default = "") 

    args = parser.parse_args()

    file_dir_list = []
    if args.id_file == "": 
        for id in args.id:
            for youtubepath in os.listdir(os.path.join(args.id_path, id)):
                file_dir_list.append(os.path.join(id, youtubepath))
    else:
        file_dir_list = args.id_file

    # 1. Download all youtube video in id
    if args.download_video:
    
        for file in file_dir_list:

            os.makedirs(os.path.join(args.video_dir, file), exist_ok=True)
            print(os.path.join(args.video_dir, file))

            download_single_youtube(id = file, rank = args.rank, path=os.path.join(args.video_dir, file), pytube_flag=args.pytube)
  
    # 2. Extract all Frame Images from all Videos
    if args.video_to_frame:
        for file in file_dir_list:
            path = os.path.join(args.video_dir, file)
    if args.video_to_frame:
        for file in file_dir_list:
            path = os.path.join(args.video_dir, file)

            video_path = os.path.join(path, os.listdir(path)[0])
            print(f'video_path : {video_path}')

            cap = cv2.VideoCapture(video_path)

            print(f'width : {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}')
            print(f'height : {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}')
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count/fps
            print(f'frame length : {fps}')
            print(f'frame count : {frame_count}')
            print(f'frame length : {duration}')


            if len(glob.glob(os.path.join(args.video_dir, file, '*.png'))) == int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) :
                print(f'pass ! {video_path} \n')
                continue

            for framenum in range(0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):

                cap.set(cv2.CAP_PROP_FRAME_COUNT, framenum)
                ret,frame = cap.read()
                if ret is False:
                    break
                
                if framenum % 1000 ==0:
                    print(f'framenum : {framenum}')
                    
                # Image Processing
                cv2.imwrite(path + '/' + str(framenum).zfill(5) + '.png', frame)

                k = cv2.waitKey(1) & 0xff
                if k == 27: # Escape (ESC)
                    break
        

            cap.release()

    # 3. Extract Specific Frame Images by Text File
    if args.frame_by_txt:

        for file in file_dir_list:
            path = os.path.join(args.video_dir, file)
                
            video_path = os.path.join(path, os.listdir(path)[0])
            print(f'video_path : {video_path}')

            cap = cv2.VideoCapture(video_path)

            print(f'width : {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}')
            print(f'height : {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}')
            print(f'frame length : {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}')
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count/fps
            print(f'frame length : {fps}')
            print(f'frame count : {frame_count}')
            print(f'frame length : {duration}')

            # txt list
            txt_list = os.listdir(os.path.join(args.id_path, file))
            frame_list = []

            # 주요 scene의 시작 frame과 끝 frame을 list에 저장
            for txt in txt_list:
                f = open(os.path.join(args.id_path, file, txt))
                text_list = list(enumerate(f))
                frame_list.append(int(text_list[7][1].split(' ')[0]))
                frame_list.append(int(text_list[-1][1].split(' ')[0]))

            frame_list = sorted(frame_list)
            print(f"frame list : {frame_list}")

            if fps != 25:
                frame_list = [ int(i * cap.get(cv2.CAP_PROP_FPS)/25 + 1) for i in frame_list]
                print(f"frame list ({fps}/25) : {frame_list}")

            i = 0
            len_frame_list = int(len(frame_list)/2)

            for framenum in range(0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):

                cap.set(cv2.CAP_PROP_FRAME_COUNT, framenum)
                ret,frame = cap.read()
                if ret is False:
                    break
                
                if framenum >= frame_list[2*i] and framenum < frame_list[2*i+1]:
                    cv2.imwrite(path + '/' + str(framenum).zfill(5) + '.png', frame)
                elif framenum == frame_list[2*i+1]:
                    print(framenum)
                    cv2.imwrite(path + '/' + str(framenum).zfill(5) + '.png', frame)
                    if i == (len_frame_list-1):
                        break
                    i = i+1

                k = cv2.waitKey(1) & 0xff
                if k == 27: # Escape (ESC)
                    break