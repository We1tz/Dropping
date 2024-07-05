import React from 'react';

function Navbar() {
    return (
        <div>
            <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Foxproof</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarColor02">
                        <ul class="navbar-nav me-auto">
                            <li class="nav-item">
                                <a data-testid="home-link" class="nav-link active" href="/">Главная</a>
                            </li>
                            <li>
                            <a data-testid="home-link" class="nav-link active" href="/rating">Рейтинг</a>
                            </li>
                            <li>
                            <a data-testid="home-link" class="nav-link active" href="/victorine">Викторина</a>
                            </li>
                            <li>
                            <a data-testid="home-link" class="nav-link active" href="/graph">Аналитика</a>
                            </li>
                        </ul>
                            <a data-testid="home-link" class="nav-link text-light" href="/register">Регистрация</a>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Navbar;