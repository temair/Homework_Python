import io
import dlib
import numpy as np
from skimage import io as skio
import nmslib
from PIL import Image
from config import path_jpg
import os

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_rec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
indexs = {}
query_time_params = {'efSearch': 400}

for something in os.listdir('./sity'):
    if os.path.isdir(f'./sity/{something}'):
        indexs[something] = nmslib.init(method='hnsw', space='l2',data_type=nmslib.DataType.DENSE_VECTOR)

for something in os.listdir('./sity'):
        if os.path.isdir(f'./sity/{something}'):
            for files in os.listdir(f'./sity/{something}'):
                if files == 'embeddings.bin':
                    print(something)
                    indexs[something].loadIndex(f'{path_jpg}/{something}/embeddings.bin')
                    indexs[something].setQueryTimeParams(query_time_params)

def get_face_descriptor(photo, detector, sp, face_rec):
	img = skio.imread(photo)
	win1 = dlib.image_window()
	win1.clear_overlay()
	win1.set_image(img)
	face_descriptor = None
	shape = None
	detected_faces = detector(img, 1)
	for k, d in enumerate(detected_faces):
		shape = sp(img, d)
		win1.clear_overlay()
		win1.add_overlay(d)
		win1.add_overlay(shape)
	try:
		face_descriptor = face_rec.compute_face_descriptor(img, shape)
		face_descriptor = np.asarray(face_descriptor)
	except:
		pass
	return face_descriptor, detected_faces


def crop_face(photo, d):
    detected_face_photo = Image.open(photo)
    detected_face_photo = detected_face_photo.crop((d.left(), d.top(), d.right(), d.bottom()))
    out = io.BytesIO()
    out.name = f'output.png'
    detected_face_photo.save(out)
    output = io.BytesIO(out.getvalue())
    return types.InputFile(path_or_bytesio=output)

def recognition(photo, data):
	embedding, d = get_face_descriptor(photo, detector, sp, face_rec)
	try:
		a = indexs[data].knnQuery(embedding, 3)
	except IndexError:
		return 'NoFace'
	if not a:
		return 'NoMatch'
	photo.seek(0)
	ids, dists = a
	ids = ids[::-1]
	dists = dists[::-1]
	i = len(ids)
	result = []
	while i:
		best_dx = ids[i - 1]
		s = ''
		with open(f'{path_jpg}/{data}/associations.txt', 'r') as file_:
			for line in file_:
				w = str(best_dx) + '|'
				if line.find(w) == 0:
					s = line.split('|')[1]
					break
			s = s.split('_')[0]
			for bad_symbols in ['.txt', '.npy', '\n']:
				s = s.replace(bad_symbols, '')
			result.append({'s': s, 'match': int(dists[i-1] * -100 + 100)})
			i -= 1
	return result