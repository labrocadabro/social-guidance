# Retro Etiquette AI: A Nostalgic Journey Through Mid-20th Century Social Guidance

## Project Overview

This is a nostalgic web application that provides etiquette advice drawn from mid-20th century social guidance films. The project offers a playful and educational interface for exploring social norms and communication standards from the 1950s.

### Key Features
- Interactive AI-powered advice generator
- Vintage-inspired design with sepia-toned imagery
- Random question generation
- Responsive web application built with Nuxt 3 and Vue

### Main Purpose
The application serves as a unique platform to:
- Explore historical social etiquette and communication guidelines
- Provide entertaining and sometimes amusing advice based on mid-century social norms
- Demonstrate an innovative use of AI and historical content

### Technical Highlights
- Powered by Gradient AI for dynamic response generation
- Built with modern web technologies (Nuxt 3, Vue 3, Tailwind CSS)
- Server-side API handling for AI-generated responses
- Engaging user interface with retro-themed design

## Getting Started, Installation, and Setup

### Prerequisites

- Node.js (version 18.x or later recommended)
- A package manager: npm, pnpm, yarn, or bun

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Install dependencies:
```bash
# Choose one of the following based on your preferred package manager
npm install
# OR
pnpm install
# OR
yarn install
# OR
bun install
```

### Local Development

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev

# bun
bun run dev
```

### Building for Production

To create a production build:

```bash
# npm
npm run build

# pnpm
pnpm run build

# yarn
yarn build

# bun
bun run build
```

### Previewing Production Build

After building, preview the production version locally:

```bash
# npm
npm run preview

# pnpm
pnpm run preview

# yarn
yarn preview

# bun
bun run preview
```

### Project Initialization

The project is set up with:
- Nuxt 3
- Vue 3
- Tailwind CSS
- Vue Router

### Recommended Development Environment

- Use Visual Studio Code or WebStorm
- Install Vue and Nuxt extensions for better development experience
- Ensure Node.js and your chosen package manager are up to date

## Deployment

### Deployment Options

#### Local Deployment
1. Build the application:
```bash
npm run build
```

2. Preview the production build locally:
```bash
npm run preview
```

#### Production Deployment
##### Vercel
This Nuxt.js application is optimized for deployment on Vercel:
- Connect your GitHub repository to Vercel
- Vercel will automatically detect the Nuxt.js project
- Configure deployment settings in the Vercel dashboard

##### Netlify
To deploy on Netlify:
1. Install Netlify CLI:
```bash
npm install netlify-cli -g
```

2. Build the application:
```bash
npm run generate
```

3. Deploy to Netlify:
```bash
netlify deploy
```

##### Docker Deployment
1. Build the Docker image:
```bash
docker build -t nuxt-app .
```

2. Run the Docker container:
```bash
docker run -p 3000:3000 nuxt-app
```

#### Recommended Hosting Platforms
- Vercel (Recommended)
- Netlify
- DigitalOcean App Platform
- Heroku

#### Important Notes
- Ensure all environment variables are properly configured
- Use `npm run build` for server-side rendering
- Use `npm run generate` for static site generation

## Feature Highlights

The application provides an interactive platform for exploring mid-20th century social etiquette through an AI-powered advice generator. Key features include:

### Retro-Styled Advice Interface
- Vintage-inspired design with sepia-toned imagery and nostalgic aesthetics
- Responsive textarea for submitting etiquette-related questions
- Stylized UI elements that evoke mid-20th century design sensibilities

### AI-Powered Advice Generation
- Real-time advice generation using machine learning models
- Retrieval-Augmented Generation (RAG) for contextually relevant responses
- Leverages a curated dataset of social guidance film transcripts

### Interactive User Experience
- Ability to submit custom questions about social etiquette
- "Random Question" button for spontaneous advice exploration
- Error handling and loading state management
- Smooth transitions between question submission and response display

### Context and Learning
- Access to a dedicated "About" page explaining social guidance films
- Powered by a comprehensive dataset of historical social instruction materials

## Configuration

### Project Configuration

#### Framework and Core Settings
- **Framework**: Nuxt.js (version 3.11.2)
- **Vue.js**: Version 3.4.21
- **Module Type**: ECMAScript Module (ESM)

#### Styling and Design
- **CSS Framework**: Tailwind CSS
- **Custom Color Palette**:
  - Sepia Tones:
    - Light: `#f7f6e4`
    - Medium: `#EAD9C0`
    - Dark: `#4E2310`
  - Accent Color: `#e45034`

#### Typography
- **Header Font**: Playfair Display
- **Body Font**: Roboto Serif
- **Accent Font**: Peralta

#### Modules and Plugins
- **Tailwind CSS Module**: `@nuxtjs/tailwindcss`
- **Google Fonts Module**: `@nuxtjs/google-fonts`

#### Development Scripts
- `dev`: Start development server
- `build`: Compile production build
- `generate`: Generate static site
- `preview`: Preview production build
- `start`: Run production server

#### Build Configuration
- Nuxt DevTools: Enabled
- PostCSS and Tailwind CSS integration
- Automatic font loading via Google Fonts module

#### Customization Notes
- Custom font families defined in Tailwind configuration
- Extended color palette with sepia and accent colors
- Responsive design enabled through Tailwind CSS

## Project Structure

The project is structured as follows:

### Root Directory
- Configuration files for project setup and development:
  - `package.json`: Defines project dependencies and scripts
  - `nuxt.config.ts`: Nuxt.js configuration
  - `tailwind.config.ts`: Tailwind CSS configuration
  - `.gitignore`: Specifies intentionally untracked files
  - `tsconfig.json`: TypeScript configuration

### Pages
Located in the `pages/` directory:
- `index.vue`: Main landing page
- `about.vue`: About page of the application

### Components
Stored in the `components/` directory:
- `clock-spinner.vue`: A reusable UI component, likely for loading or progress indication

### Assets
In the `assets/` directory:
- CSS: `css/tailwind.css` for styling
- Images: 
  - Human profile images (man/woman variations in normal and sepia)

### Dataset
A comprehensive `dataset/` directory with multiple subdirectories:
- `json/`: Contains numerous JSON files for data processing
- `prompts/`: Text files potentially containing prompt templates
- `q-and-a/`: Question and answer text files
- `transcripts/`: Transcript text files
- Python scripts for data manipulation:
  - `extract_questions.py`
  - `generate_content.py`
  - `gradient_finetune.py`
  - `gradient_query.py`
  - `jsonify.py`
  - `promptify.py`

### Server
In the `server/` directory:
- `api/completion.post.ts`: API endpoint for handling completions
- `tsconfig.json`: TypeScript configuration for server-side code

### Public
`public/` directory contains:
- `favicon.ico`: Website favicon

The project appears to be a Nuxt.js application with a focus on dataset processing and potentially an AI-driven interaction or content generation system.

## Technologies Used

### Frontend
- [Vue.js](https://vuejs.org/) (v3.4.21)
- [Nuxt.js](https://nuxt.com/) (v3.11.2)
- [Vue Router](https://router.vuejs.org/) (v4.3.0)

### Styling
- [Tailwind CSS](https://tailwindcss.com/) (via @nuxtjs/tailwindcss)
- Custom color and font configurations

### Fonts
- Google Fonts integration
  - Yesteryear
  - Peralta
  - Roboto Serif
  - Playfair Display

### Development Tools
- Nuxt DevTools
- TypeScript support

## Additional Notes

### AI-Powered Vintage Advice Platform

This project is a unique web application that provides etiquette advice from mid-20th century social guidance films using AI technology. The application leverages retrieval-augmented generation (RAG) to deliver contextually accurate responses based on historical social etiquette materials.

#### Key Features
- Interactive Q&A interface with vintage aesthetic
- AI-powered responses generated from historical social guidance content
- Random question generation
- Retro-inspired design with sepia-toned imagery

#### External Dependencies
- Gradient AI for language model and retrieval-augmented generation
- Nuxt.js for frontend framework
- Tailwind CSS for styling
- Google Fonts for typography

#### Data and Content
The application uses a curated dataset of mid-20th century social guidance film transcripts, which serve as the knowledge base for generating contextually appropriate advice.

#### Ethical Considerations
While the application provides historical social guidance, users should understand that the advice reflects mid-20th century social norms and may not align with contemporary perspectives on social interaction and interpersonal relationships.

#### Performance and Scalability
The application uses client-side rendering with Nuxt.js and server-side API handling, allowing for efficient response generation and a smooth user experience.

## Contributing

We welcome contributions to this project! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### Getting Started

1. Fork the repository
2. Clone your forked repository locally
3. Create a new branch for your contribution

### Prerequisites

- Node.js (recommended version: latest LTS)
- npm, pnpm, yarn, or bun

### Development Workflow

#### Installing Dependencies
Use your preferred package manager to install dependencies:

```bash
npm install
# or
yarn install
# or
pnpm install
# or
bun install
```

#### Running the Project
Start the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun run dev
```

### Contribution Guidelines

#### Code Style
- Follow Vue.js and Nuxt.js best practices
- Use consistent indentation (2 spaces)
- Maintain clean, readable, and commented code
- Adhere to existing code structure and patterns

#### Commit Messages
- Use clear and descriptive commit messages
- Follow conventional commit format if possible (e.g., `feat:`, `fix:`, `docs:`)

#### Pull Request Process
1. Ensure your code passes all existing tests
2. Update documentation if your changes affect existing functionality
3. Add new tests for any added features
4. Submit a pull request with a clear description of changes

### Reporting Issues
- Use GitHub Issues to report bugs or suggest enhancements
- Provide detailed information, including:
  - Steps to reproduce the issue
  - Expected vs. actual behavior
  - Relevant error messages
  - Your environment details (OS, Node.js version, etc.)

### Code of Conduct
Please be respectful and inclusive. Harassment and discrimination are not tolerated.

### Questions?
If you have questions about contributing, please open an issue for discussion.

## License

This project is currently unlicensed. By default, this means that the original author retains all copyright, and no one else may reproduce, distribute, or create derivative works without explicit permission.

#### Implications
- No one can legally use, modify, or share this code without the owner's consent
- There are no explicit permissions granted to users or developers
- Potential collaborators or users should contact the project owner for specific usage rights

**Recommendation**: Consider adding an open-source license to clarify usage terms and encourage collaboration.