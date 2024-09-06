from PIL import Image
import pytesseract

# Tesseract OCR의 경로 설정 (시스템에 맞는 경로로 설정)
# 예시 (Windows):
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지를 로드
image_path = './user_image/image.png'
image = Image.open(image_path)

# 관심 영역(ROI) 좌표 정의 (왼쪽 위 x, 왼쪽 위 y, 오른쪽 아래 x, 오른쪽 아래 y)
# 예: (x1, y1, x2, y2)
roi = (100, 100, 400, 400)  # 원하는 좌표에 맞춰 수정

# 이미지에서 관심 영역을 자름
cropped_image = image.crop(roi)

# OCR을 통해 텍스트 추출
text = pytesseract.image_to_string(image, lang='kor+eng')

# 추출된 텍스트 출력
print("추출된 텍스트:", text)
