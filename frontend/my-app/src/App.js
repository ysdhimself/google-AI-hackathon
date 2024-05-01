import logo from './logo.svg';
import './App.css';
import './normal.css';

function App() {
  return (
    <div className="App">
      <aside className = "sidemenu">
          <div className = "sidemenubutton">
            <span>+</span>
            New chat
          </div>
      </aside>
      
      <section className = "chatbot">
        <div className='chatlog'>
          <div className='chatmessage'>
            <div className='chatmessagecenter'>
              <div className='avatar'>
                  
              </div>
              <div className='message'>
                  hi
              </div>
            </div>
            <div className='chatmessageAI'>
            <div className='chatmessagecenter'>
              <div className='avatarAI'>
                  
              </div>
              <div className='message'>
                  I am AI
              </div>
            </div>
          </div>
          </div>
        </div>
        <div className='chatinputholder'>
          <textarea rows = '1' 
          className='chatinput'>
          </textarea>
        </div>
      </section>


    </div>
  );
}

export default App;
