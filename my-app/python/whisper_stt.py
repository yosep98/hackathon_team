import sys
from faster_whisper import WhisperModel

# 1. 인자 체크
if len(sys.argv) < 2:
    print("오디오 파일 경로를 인자로 넣어주세요.")
    sys.exit(1)

audio_path = sys.argv[1]

try:
    # 2. 모델 로딩 (M1 맥에 적합한 설정)
    model = WhisperModel("base", device="cpu", compute_type="int8")  # or device="auto"

    # 3. 오디오 STT 수행
    segments, _ = model.transcribe(audio_path)

    # 4. 텍스트 병합 및 출력
    results = [segment.text.strip() for segment in segments]
    final_result = " ".join(results)

    print(final_result)

except Exception as e:
    print(f"[ERROR] Whisper 실행 중 오류 발생: {e}")
    sys.exit(1)
