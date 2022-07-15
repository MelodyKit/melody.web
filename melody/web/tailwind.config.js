const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
    content: ["./**/*.html"],
    darkMode: "media",
    theme: {
        extend: {
            colors: {
                "melody-purple": "#cc55ff",
                "melody-blue": "#55ccff"
            },
            fontFamily: {
                sans: ["Gotham Pro", ...defaultTheme.fontFamily.sans]
            }
        }
    }
}
