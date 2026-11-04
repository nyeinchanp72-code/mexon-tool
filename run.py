import importlib.util
import sys
import asyncio

# တည်ဆောက်ထွက်လာသော .so ဖိုင်အမည်ကို ဤနေရာတွင် ထည့်ပါ
so_file = "new_mk_2.cpython-314-aarch64-linux-android.so"

try:
    spec = importlib.util.spec_from_file_location("new_mk_2", so_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["new_mk_2"] = module
    spec.loader.exec_module(module)

    if hasattr(module, "main"):
        asyncio.run(module.main())
    else:
        print("❌ Main function not found in module.")
except Exception as e:
    print(f"❌ Error loading binary: {e}")
