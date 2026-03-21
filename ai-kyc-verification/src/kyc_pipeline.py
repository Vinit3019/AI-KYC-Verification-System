from face_match import compare_faces
from ocr_extraction import extract_text

id_image = "../dataset/id_card.jpg"
selfie_image = "../dataset/selfie.jpg"

print("Running OCR...")
text = extract_text(id_image)
print(text)

print("Running Face Verification...")
match = compare_faces(id_image, selfie_image)

if match:
    print("KYC Verification SUCCESS")
else:
    print("KYC Verification FAILED")