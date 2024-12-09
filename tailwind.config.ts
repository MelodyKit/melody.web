import defaultTheme from "tailwindcss/defaultTheme";

export default {
  content: ["./src/**/*.rs"],
  darkMode: "media",
  theme: {
    extend: {
      colors: {
        // melody
        "melody-purple": "#cc55ff",
        "melody-blue": "#55ccff",
        // brands
        discord: "#5865f2",
        youtube: "#ff0000",
        reddit: "#ff5700",
        telegram: "#229ed9",
      },
      fontFamily: {
        sans: ["Gotham Pro", ...defaultTheme.fontFamily.sans],
      },
    },
  },
};
