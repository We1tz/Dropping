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
                        <a href="https://t.me/antidropping_bot" class="text-white me-4">
                            <i class="fab fa-brands fa-telegram"></i>
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
                            
                            <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                                <h6 class="text-uppercase fw-bold">Контакты</h6>
                                <hr
                                    class="mb-4 mt-0 d-inline-block mx-auto"
                                />
                                <p><i class="fas fa-envelope mr-3"></i> support@antidropping.ru</p>
                            </div>
                        </div>
                    </div>
                </div>
            </footer>

        </div> 
    );
}

export default HomeFooter;