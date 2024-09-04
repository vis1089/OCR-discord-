import cv2
import numpy as np

# 포지션 분류 (FW, MF, DM, DF, FB, GK)
def position(pos):
    match pos:
        case "CAM" | "CM" | "LM" | "RM" | "LCM" | "RCM":
            return "MF"
        case "CDM" | "LDM" | "RDM":
            return "DM"
        case "CB" | "LCB" | "RCB":
            return "DF"
        case "LB" | "RB" | "LWB" | "RWB":
            return "FB"
        case "GK":
            return "GK"
        case _:
            return "FW"


# 사진 분류(유효한 사진인지 확인) - 
def check_image(user_img):
    check_img = "./img/check.png"
    
    userImg = cv2.imread(user_img)
    checkImg = cv2.imread(check_img)

    if userImg is None or checkImg is None:
        raise ValueError("이미지를 로드할 수 없습니다. 경로를 확인하세요.")

    # p2 이미지를 p1에서 찾기 (템플릿 매칭)
    result = cv2.matchTemplate(userImg, checkImg, cv2.TM_CCOEFF_NORMED)

     # 최대 일치 지점 및 그 위치 찾기
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # 일치가 잘 되었는지 임계값으로 확인 (예: 0.8 이상이면 일치했다고 간주)
    threshold = 0.1
    print(max_val)
    print(max_loc)
    if max_val >= threshold:
        print(f"p2 이미지가 p1 이미지 내에서 발견되었습니다. 위치: {max_loc}")
        return True
    else:
        print("p2 이미지가 p1 이미지 내에서 발견되지 않았습니다.")
        return False


# 사진 분류(요약, 선수 이름 등)

def find_and_save_image(p1_path, p2_path, output_path):
    # p1과 p2 이미지를 로드
    p1 = cv2.imread(p1_path)
    p2 = cv2.imread(p2_path)

    if p1 is None or p2 is None:
        raise ValueError("이미지를 로드할 수 없습니다. 경로를 확인하세요.")

    # p2 이미지를 p1에서 찾기 (템플릿 매칭)
    result = cv2.matchTemplate(p1, p2, cv2.TM_CCOEFF_NORMED)
    
    # 최대 일치 지점 및 그 위치 찾기
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # 일치가 잘 되었는지 임계값으로 확인 (예: 0.8 이상이면 일치했다고 간주)
    threshold = 0.8
    if max_val >= threshold:
        print(f"p2 이미지가 p1 이미지 내에서 발견되었습니다. 위치: {max_loc}")
        
        # p1 이미지를 전체 저장
        cv2.imwrite(output_path, p1)
        print(f"p1 이미지가 {output_path}에 저장되었습니다.")
    else:
        print("p2 이미지가 p1 이미지 내에서 발견되지 않았습니다.")


