"""
Test script to verify Python environment is working correctly.
"""

def main():
    import sys
    print("=" * 60)
    print("Python Environment Test")
    print("=" * 60)
    print(f"\n[OK] Python Version: {sys.version}")
    print(f"[OK] Python Path: {sys.executable}")
    print(f"[OK] Working Directory: {sys.path[0]}")
    
    print("\n" + "=" * 60)
    print("Testing Package Imports")
    print("=" * 60)
    
    packages = [
        ('numpy', 'NumPy'),
        ('matplotlib', 'Matplotlib'),
        ('pandas', 'Pandas'),
        ('pymatgen', 'Pymatgen'),
        ('ase', 'ASE'),
        ('networkx', 'NetworkX'),
        ('mp_api', 'Materials Project API'),
        ('torch', 'PyTorch'),
    ]
    
    success_count = 0
    for module_name, display_name in packages:
        try:
            module = __import__(module_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"[OK]   {display_name:25} v{version}")
            success_count += 1
        except ImportError as e:
            print(f"[FAIL] {display_name:25} NOT INSTALLED")
        except Exception as e:
            print(f"[WARN] {display_name:25} ERROR: {e}")
    
    print("\n" + "=" * 60)
    print(f"Results: {success_count}/{len(packages)} packages working")
    print("=" * 60)
    
    if success_count == len(packages):
        print("\nAll packages are working perfectly!")
    elif success_count >= len(packages) - 1:
        print("\nEnvironment is mostly ready!")
        print("Note: PyTorch may need Visual C++ Redistributable")
        print("   Download: https://aka.ms/vs/17/release/vc_redist.x64.exe")
    else:
        print("\nSome packages are missing. Run: uv sync")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
