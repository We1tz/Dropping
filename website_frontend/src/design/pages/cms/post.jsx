import React, { useEffect, useState } from 'react'
import HomeFooter from '../../awesome-components/footers/footer-home'
import HomeTemplate from '../../awesome-templates/home-template'
import { useParams } from 'react-router-dom';
import files from '../../../../public/index.json';
import {remark} from'remark';
import html from'remark-html';

export default function Post() {

    const [post, setPost] = useState('');
    const { id } = useParams();
    const [content, setContent] = useState("");
    
    async function fetchData() {
        fetch("../../../../public/posts/"+id+".md")
                    .then(res => res.text())
                    .then(res =>  setContent(res))
                    .catch(err => console.log(err));

        const processedContent = await remark()
            .use(html)
            .process(content);
        setPost(processedContent.toString());            
    }

    useEffect(() => {
        fetchData();
        
    });
  return (
    <>
        <HomeTemplate>
            <div className='text-white'>
            <section class=" section-article section-fullwindow">
                    <div class="jumbotron jumbotron-fluid text-start">
                        <div dangerouslySetInnerHTML={{__html: post}}></div>
                    </div>
                </section>
            </div>
        </HomeTemplate>
        <HomeFooter />
    </>
  )
}
//Елена из медси сигма