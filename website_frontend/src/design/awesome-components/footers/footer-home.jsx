import React from 'react';

function HomeFooter() {
    return (
        <div>
            <br />
            <br /><br />
            <footer class="text-center bg-dark text-lg-start text-light footer">
                <div
                    class="d-flex justify-content-between p-4 bg-dark"
                >
                    <div class=" text-light">
                        <span>Наши социальные сети:</span>
                    </div>
                    <div>
                        <a href="https://t.me/antidropping_bot" class="text-white me-4">
                            <i class="fab fa-brands fa-telegram"></i>
                        </a>
                         <a href="mailto:support@antidropping.ru" class="text-white me-4"><i class="fas fa-envelope mr-3"/></a>
                    </div>
                </div>
            </footer>

        </div> 
    );
}

export default HomeFooter;