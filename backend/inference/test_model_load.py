import os
import traceback

def main():
    try:
        from ultralytics import RTDETR
        print('ultralytics imported')
    except Exception as e:
        print('FAILED to import ultralytics:', e)
        traceback.print_exc()
        return

    try:
        model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'best.pt'))
        print('Model path:', model_path)
        if not os.path.exists(model_path):
            print('Model file does not exist at path')
            return

        # Load model (CPU)
        model = RTDETR(model_path)
        print('Model loaded:', type(model))

        names = getattr(model, 'names', None)
        print('Model names:', names)

        # Try to access underlying torch module for param count
        total_params = None
        try:
            underlying = getattr(model, 'model', None)
            if underlying is not None:
                total_params = sum(p.numel() for p in underlying.parameters())
        except Exception:
            total_params = None

        print('Total params (approx):', total_params)

    except Exception as e:
        print('Error while loading or inspecting model:', e)
        traceback.print_exc()

if __name__ == '__main__':
    main()
