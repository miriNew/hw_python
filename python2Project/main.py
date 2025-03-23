import time

# ✅ דקורטור לחישוב זמן ריצה (מתוקן לתמוך בפרמטרים)
def my_decorator(func):
    def wrapper(*args, **kwargs):  # תמיכה בפרמטרים
        temp1 = time.time()
        result = func(*args, **kwargs)  # קריאה לפונקציה עם הפרמטרים
        temp2 = time.time()
        print(f"executed {temp2 - temp1:.5f} seconds")
        return result  # מחזיר את תוצאת הפונקציה
    return wrapper  # מחזיר את הפונקציה החדשה

# ✅ פונקציה לדוגמה
@my_decorator
def my_function():
    time.sleep(1)
    print("Function executed")

# קריאה לפונקציה
my_function()

# ✅ דקורטור Cache (מתוקן)
def cache_decorator(func):
    cache = {}  # מילון לאחסון חישובים קודמים

    def wrapper(*args):  # תמיכה בפרמטרים
        if args in cache:
            return cache[args]  # מחזיר תוצאה מהזיכרון

        result = func(*args)  # חישוב חדש
        cache[args] = result  # שמירת התוצאה ב-cache
        return result

    return wrapper  # מחזיר את הפונקציה החדשה

# ✅ חישוב פיבונאצי עם Cache + מדידת זמן (סדר הדקורטורים חשוב!)
@my_decorator
@cache_decorator
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# ✅ השוואת ביצועים
n = 35
print("\n🟢 חישוב Fibonacci עם Cache:")
fibonacci_cached(n)
