// توی موبایل hover نداریم. برای همین با کلیک (یا لمس) روی کارت،
// بین عکس اول و عکس دوم جابه‌جا می‌شیم.

// ۱) کانتینری رو می‌گیریم که همه‌ی کارت‌ها توشه (از items.html)
const list = document.getElementById("movie-list");

// ۲) فقط یک listener روی کانتینر می‌ذاریم، نه روی تک‌تک کارت‌ها.
//    کلیک روی هر عنصر داخلی به سمت بالا (به کانتینر) می‌رسه (Event Bubbling).
//    این الگو اسمش Event Delegation هست.
list.addEventListener("click", event => {
    // ۳) event.target همون عنصریه که واقعاً کلیک شده (مثلاً یه <img>).
    //    closest(".movie") از اون عنصر به سمت بالا می‌گرده و کارتی رو پیدا می‌کنه
    //    که عنصر داخلش بوده. اگه بیرون از کارت‌ها کلیک شده باشه نتیجه null می‌شه.
    const movie = event.target.closest(".movie");

    // ۴) فقط وقتی واقعاً یه کارت پیدا شد...
    if (movie) {
        // ۵) ...کلاس CSS به اسم "flipped" رو روشن/خاموش می‌کنیم.
        //    CSS هم وقتی .flipped هست، عکس دوم رو نشون می‌ده.
        movie.classList.toggle("flipped");
    }
});