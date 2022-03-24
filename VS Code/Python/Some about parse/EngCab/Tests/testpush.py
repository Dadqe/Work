import win10toast
 
toaster = win10toast.ToastNotifier()
toaster.show_toast("WARNING", "Появилось новая заявка")
print("Тостер сработал")