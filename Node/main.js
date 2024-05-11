function minPagesToRead(pages, days) {
    let left = 1;
    let right = Math.max(...pages);
    let result = -1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        
        if (isValid(pages, mid, days)) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return result;
}

function isValid(pages, x, days) {
    let remainingDays = days;

    for (let i = 0; i < pages.length; i++) {
        remainingDays -= Math.ceil(pages[i] / x);
        if (remainingDays < 0) {
            return false;
        }
    }

    return true;
}

// Example usage:
const pages = [5, 3, 4];
const days = 4;
const minPagesPerDay = minPagesToRead(pages, days);
console.log(minPagesPerDay);