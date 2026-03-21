from deepface import DeepFace

def compare_faces(id_image, selfie_image):
    try:
        result = DeepFace.verify(id_image, selfie_image)
        return result["verified"]
    except Exception as e:
        print("Face verification error:", e)
        return False