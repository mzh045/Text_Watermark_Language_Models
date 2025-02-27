from models.watermark_faster import watermark_model
from options import get_parser_main_model
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

def watermark_embed_demo(raw):
    watermarked_text = model.embed(raw)
    return watermarked_text

def watermark_extract(raw):
    is_watermark, p_value, n, ones, z_value = model.watermark_detector_fast(raw)
    confidence = (1 - p_value) * 100
    return f"{confidence:.2f}%"

def precise_watermark_detect(raw):
    is_watermark, p_value, n, ones, z_value = model.watermark_detector_precise(raw)
    confidence = (1 - p_value) * 100
    return f"{confidence:.2f}%"

if __name__ == "__main__":
    opts = get_parser_main_model().parse_args()
    model = watermark_model(language=opts.language, mode=opts.mode, tau_word=opts.tau_word, lamda=opts.lamda)
    
    while True:
        print("\n" + "=" * 60)
        print("Watermarking Text Generated by Black-Box Language Models".center(60))
        print("Created by Xi Yang (yx9726@mail.ustc.edu.cn)".center(60))
        print("=" * 60 + "\n")

        print("1. Inject Watermark")
        print("2. Detect Watermark")
        print("3. Exit\n")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\n" + "-" * 60)
            text = input("Enter the text to embed a watermark: ")
            watermarked_text = watermark_embed_demo(text)
            print("\n" + "-" * 60)
            print(f"Watermarked Text:\n{watermarked_text}")
            print("-" * 60)

        elif choice == '2':
            print("\n" + "-" * 60)
            text = input("Enter the text to analyze: ")
            mode = input("Select detection mode (Fast/Precise): ")

            if mode.lower() == 'fast':
                confidence = watermark_extract(text)
            elif mode.lower() == 'precise':
                confidence = precise_watermark_detect(text)
            else:
                print("Invalid mode. Please choose 'Fast' or 'Precise'.")
                continue

            print("\n" + "-" * 60)
            print(f"Confidence (the likelihood of the text containing a watermark): {confidence}")
            print("-" * 60)

        elif choice == '3':
            print("\nExiting...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
