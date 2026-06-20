class Slider {
    constructor(container) {
        this.container = container;
        this.track = container.querySelector('.slider-track');
        this.slides = container.querySelectorAll('.slider-slide');
        this.prevBtn = container.querySelector('.slider-prev');
        this.nextBtn = container.querySelector('.slider-next');
        this.dots = container.querySelectorAll('.slider-dot');
        this.current = 0;
        this.total = this.slides.length;
        this.interval = null;

        if (this.total === 0) return;

        this.init();
    }

    init() {
        if (this.nextBtn) this.nextBtn.addEventListener('click', () => this.next());
        if (this.prevBtn) this.prevBtn.addEventListener('click', () => this.prev());
        this.dots.forEach((dot, i) => {
            dot.addEventListener('click', () => this.goTo(i));
        });
        this.updateDots();
        this.startAutoPlay();

        this.container.addEventListener('mouseenter', () => this.stopAutoPlay());
        this.container.addEventListener('mouseleave', () => this.startAutoPlay());
    }

    goTo(index) {
        this.current = index;
        if (this.track) {
            this.track.style.transform = `translateX(-${index * 100}%)`;
        }
        this.updateDots();
    }

    next() {
        this.goTo((this.current + 1) % this.total);
        this.resetAutoPlay();
    }

    prev() {
        this.goTo((this.current - 1 + this.total) % this.total);
        this.resetAutoPlay();
    }

    updateDots() {
        this.dots.forEach((dot, i) => {
            if (i === this.current) {
                dot.classList.remove('bg-white/50');
                dot.classList.add('bg-white');
            } else {
                dot.classList.remove('bg-white');
                dot.classList.add('bg-white/50');
            }
        });
    }

    startAutoPlay() {
        if (this.interval) return;
        this.interval = setInterval(() => this.next(), 3000);
    }

    stopAutoPlay() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }

    resetAutoPlay() {
        this.stopAutoPlay();
        this.startAutoPlay();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.slider-container').forEach(el => new Slider(el));
});
