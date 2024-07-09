import React from 'react';

function HomeFooter() {
    return (
        <div>
            
            <footer class="text-center bg-dark text-lg-start text-light footer">
                <div
                    class="d-flex justify-content-between p-4 bg-dark"
                >
                    <div class="me-5 text-light">
                        <span>Наши социальные сети:</span>
                    </div>
                    <div>
                        <a href="" class="text-white me-4">
                            <i class="fab fa-brands fa-telegram"></i>
                        </a>
                        <a href="https://github.com/We1tz/Dropping" class="text-white me-4">
                            <i class="fab fa-github"></i>
                        </a>
                    </div>
                </div>
                <div class="">
                    <div class="container text-center text-md-start mt-5">
                        <div class="row mt-3">
                            <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                                <h6 class="text-uppercase fw-bold">Foxproof</h6>
                                <hr
                                    class="mb-4 mt-0 d-inline-block mx-auto"
                                />
                                <p>
                                    Сервис для выявления финансового мошенничества
                                </p>
                            </div>
                            <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                                <h6 class="text-uppercase fw-bold">Продукты нашей IT-империи</h6>
                                <hr
                                    class="mb-4 mt-0 d-inline-block mx-auto"
                                />
                                <p>
                                    <a href="https://github.com/We1tz/Dropping" class="text-white">Foxproof</a>
                                </p>
                            </div>
                            
                            <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                                <h6 class="text-uppercase fw-bold">Контакты</h6>
                                <hr
                                    class="mb-4 mt-0 d-inline-block mx-auto"
                                />
                                <p><i class="fas fa-home mr-3"></i> Олимпийский просп., 1, Сочи, Краснодарский край, 354340</p>
                                <p><i class="fas fa-envelope mr-3"></i> help@sochisirius.ru</p>
                                <p><i class="fas fa-phone mr-3"></i> +8 (800)-100-76-63</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div
                    class="text-center p-3"
                >
                    © 2024 Copyright:
                    <a class="text-white" href="https://github.com/We1tz/Dropping"
                    >Foxproof</a>
                </div>
            </footer>

        </div> 
    );
}

export default HomeFooter;