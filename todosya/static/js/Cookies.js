export const CookiesStorage = {
    getCookies() {
        const cookies = document.cookie
            .split('; ')
            .map((cookString) => cookString.split('='));
        let data = {};
        cookies.forEach((cookie) => {
            data = { ...data, ...{ [cookie[0]]: cookie[1] } };
        });

        return data;
    },

    getItem(cookieName) {
        const data = this.getCookies();
        return data[cookieName];
    },

    setItem(cookieName, cookieValue) {
        const DateNow = new Date();

        const Day = DateNow.getDate();
        const Month = DateNow.getMonth();
        const Year = DateNow.getFullYear();

        const expires = new Date(Year, Month, Day + 10).toUTCString();

        document.cookie = `${cookieName}=${cookieValue}; domain=${
            window.location.hostname.split(':')[0]
        }; expires=${expires}; path=/;`;
    },

    removeItem(cookieName) {
        const expires = new Date().toUTCString();

        document.cookie = `${cookieName}=${null}; domain=${
            window.location.hostname.split(':')[0]
        }; expires=${expires}; path=/;`;
    },

    removeAllItems() {
        const cookieNames = Object.keys(this.getCookies());

        cookieNames.forEach((cookie) => this.removeItem(cookie));
    },
};
