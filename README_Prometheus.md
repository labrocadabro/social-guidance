# 🕰️ Nostalgia AI: Mid-Century Social Etiquette Guide

## Project Overview

A nostalgic web application that provides etiquette advice inspired by 1950s social guidance films. This unique project leverages AI to generate contextual advice based on mid-20th century social norms and expectations.

### Key Features
- Interactive AI-powered advice generator
- Randomly selectable questions about social etiquette
- Vintage-inspired user interface with sepia-toned imagery
- Responsive design using Nuxt.js and Tailwind CSS

### Purpose
The application serves as a playful exploration of mid-20th century social expectations, offering users a glimpse into historical communication norms and social guidelines. It bridges modern AI technology with vintage social instruction, creating an engaging and educational experience that highlights how social interactions and expectations have evolved over time.

## Getting Started, Installation, and Setup

### Prerequisites

- Node.js (version compatible with Nuxt 3)
- Package manager: npm, pnpm, yarn, or bun

### Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
# Choose one of the following:
npm install
# or
pnpm install
# or
yarn install
# or
bun install
```

### Development

Start the development server on `http://localhost:3000`:
```bash
# Choose one of the following:
npm run dev
# or
pnpm run dev
# or
yarn dev
# or
bun run dev
```

### Production Build

Build the application for production:
```bash
# Choose one of the following:
npm run build
# or
pnpm run build
# or
yarn build
# or
bun run build
```

### Preview Production Build

Preview the production build locally:
```bash
# Choose one of the following:
npm run preview
# or
pnpm run preview
# or
yarn preview
# or
bun run preview
```

### Additional Notes

- The project uses Nuxt 3 and Vue 3
- Tailwind CSS is integrated
- Google Fonts are configured as a dev dependency

For more detailed information about Nuxt 3, visit the [official documentation](https://nuxt.com/docs/getting-started/introduction).

## Deployment

### Deployment Options

#### Production Build

Prepare the application for production by building the static assets:

```bash
# Using npm
npm run build

# Using pnpm
pnpm run build

# Using yarn
yarn build

# Using bun
bun run build
```

#### Deployment Platforms

##### Vercel (Recommended)
- Vercel offers seamless deployment for Nuxt 3 applications
- Connect your GitHub repository
- Vercel will automatically detect the Nuxt project and configure the build settings
- Set build command: `npm run build`
- Set output directory: `.output`

##### Netlify
- Create a `netlify.toml` configuration file in the project root:
  ```toml
  [build]
    command = "npm run build"
    publish = ".output/public"
  ```
- Deploy directly from GitHub or using Netlify CLI

##### Docker
- Create a `Dockerfile` in the project root:
  ```dockerfile
  FROM node:18-alpine

  WORKDIR /app

  COPY package.json .
  COPY package-lock.json .

  RUN npm install

  COPY . .

  RUN npm run build

  EXPOSE 3000

  CMD ["npm", "start"]
  ```
- Build the Docker image:
  ```bash
  docker build -t nuxt-app .
  ```
- Run the container:
  ```bash
  docker run -p 3000:3000 nuxt-app
  ```

##### Static Hosting
- Generate static files:
  ```bash
  npm run generate
  ```
- Deploy the `.output/public` directory to any static hosting service

#### Server Deployment
For server deployment, use the start script after building:
```bash
npm run build
npm start
```

**Note:** Always refer to the [official Nuxt deployment documentation](https://nuxt.com/docs/getting-started/deployment) for the most up-to-date deployment strategies.

## Feature Highlights

The application provides an interactive web experience centered around 1950s social guidance advice, with the following key features:

### AI-Powered Advice Generation
- Interactive text input allows users to ask for vintage etiquette advice
- Utilizes AI model to generate contextual responses based on historical social guidance films
- Real-time response generation with visual loading indicator

### Dynamic Question Interaction
- "Random Question" button to automatically populate the input with a pre-defined social etiquette query
- Smooth user interface with animated form elements
- Error handling for failed API requests

### Responsive Design
- Vintage-themed visual design with sepia-toned imagery
- Adaptive layout with side images and centered content
- Integrated typography and custom UI elements

### Knowledge Base
- AI responses sourced from a curated collection of mid-20th century social guidance film transcripts
- Enables exploration of historical social norms and etiquette guidelines

## Configuration

The project uses several configuration options and modules to customize its functionality:

### Nuxt Configuration
- Nuxt DevTools are enabled for enhanced development experience
- Modules:
  - Tailwind CSS for styling
  - Google Fonts for typography

### Font Configuration
The project uses the following custom fonts:
- Header: Playfair Display
- Body: Roboto Serif
- Accent: Peralta
- Font weights: 400 and 600

### Tailwind CSS Customization
Custom theme extensions include:
- Font Families
  - Specific font assignments for header, body, and accent text
- Color Palette
  - Sepia color scheme with three variants (100, 500, 800)
  - Custom accent color (#e45034)

### Build and Development Scripts
Available scripts in `package.json`:
- `dev`: Start development server
- `build`: Build production application
- `generate`: Generate static site
- `preview`: Preview production build
- `start`: Start production server

## Project Structure

The project follows a modern web application structure with key directories and files organized for clarity and maintainability:

### Root Directory
- `package.json`: Project dependencies and scripts
- `nuxt.config.ts`: Nuxt.js configuration file
- `tailwind.config.ts`: Tailwind CSS configuration
- `tsconfig.json`: TypeScript configuration

### Source Code Directories
- `assets/`: Static assets
  - `css/`: Stylesheet files (e.g., `tailwind.css`)
  - Image files for the application

- `components/`: Vue.js component files
  - Reusable UI components (e.g., `clock-spinner.vue`)

- `data/`: Static data files
  - `questions.ts`: Likely contains predefined questions or data structures

- `dataset/`: Extensive data processing and management
  - `json/`: JSON data files
  - `prompts/`: Text prompt files
  - `q-and-a/`: Question and answer text files
  - `transcripts/`: Transcript text files
  - Python scripts for data processing:
    - `extract_questions.py`
    - `generate_content.py`
    - `gradient_finetune.py`
    - `gradient_query.py`
    - `jsonify.py`
    - `promptify.py`

- `pages/`: Nuxt.js page components
  - `index.vue`: Main landing page
  - `about.vue`: About page

- `public/`: Public assets
  - `favicon.ico`: Site favicon

- `server/`: Server-side code
  - `api/`: API route handlers (e.g., `completion.post.ts`)
  - `tsconfig.json`: Server-specific TypeScript configuration

### Frontend Framework
- Vue.js with Nuxt.js framework
- Tailwind CSS for styling
- TypeScript for type-safe development

### Key Application Files
- `app.vue`: Root Vue application component
- `error.vue`: Custom error page component

## Technologies Used

#### Frontend Framework
- [Vue.js](https://vuejs.org/) (v3.4.21)
- [Nuxt.js](https://nuxt.com/) (v3.11.2)
- [Vue Router](https://router.vuejs.org/) (v4.3.0)

#### Styling
- [Tailwind CSS](https://tailwindcss.com/) (via @nuxtjs/tailwindcss)
- Custom color palette and typography configuration

#### Fonts
- Google Fonts Integration
  - Playfair Display
  - Roboto Serif
  - Peralta
  - Yesteryear

#### Development Tools
- TypeScript
- Nuxt DevTools
- Node.js Module System (ESM)

#### Build and Deployment
- Nuxt build system
- Static site generation support
- Server-side rendering capabilities

## Additional Notes

### Font Integration

This project leverages Google Fonts for typography, including:
- Yesteryear: A decorative font
- Peralta: A playful display font
- Roboto Serif (400 weight): A versatile serif font
- Playfair Display (600 weight): An elegant serif font for headings

### Performance and Optimization

- Utilizes Nuxt 3's built-in performance optimizations
- Uses Tailwind CSS for efficient, utility-first styling
- Supports server-side rendering (SSR) and static site generation

### Development Environment

The project is configured with developer-friendly features:
- Built-in Nuxt devtools for enhanced debugging
- Supports multiple package managers (npm, pnpm, yarn, bun)
- Easy local development and production build scripts

### Customization Potential

- Easily extendable Nuxt configuration
- Flexible Tailwind CSS setup for custom design implementations
- Modular Google Fonts integration allowing quick typographic changes

### Browser and Device Compatibility

Designed with modern web standards, ensuring:
- Responsive design principles
- Cross-browser compatibility
- Mobile-first approach

## Contributing

### Ways to Contribute

We welcome contributions from the community! There are several ways you can help improve this project:

- Reporting bugs
- Suggesting enhancements
- Adding new features
- Improving documentation
- Submitting pull requests

### Getting Started

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Run tests and linting
5. Commit your changes with a clear, descriptive commit message
6. Push to your fork and submit a pull request

### Development Setup

Before contributing, ensure you have:
- Node.js installed (version compatible with Nuxt 3)
- Recommended package managers: npm, pnpm, yarn, or bun

### Coding Guidelines

- Follow Vue.js and Nuxt.js best practices
- Write clean, readable, and well-documented code
- Maintain consistent code style
- Use TypeScript for type safety
- Adhere to the project's existing code structure

### Testing

- Write tests for new features or bug fixes
- Ensure all tests pass before submitting a pull request
- Maintain or improve test coverage

### Commit Message Convention

- Use clear and descriptive commit messages
- Follow the conventional commits format if possible:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for adding or modifying tests

### Pull Request Process

1. Ensure your code passes all tests and linting
2. Update the README.md with details of changes if applicable
3. You may merge the Pull Request once it has been reviewed and approved by a maintainer

### Code of Conduct

Please be respectful and considerate of others. Harassment, discrimination, and other unethical behaviors are not tolerated.

### Questions?

If you have any questions about contributing, please open an issue for discussion.

## License

This project is currently unlicensed. 

### Implications of No License

Without a specified license, the default copyright laws apply. This means:
- The code is the exclusive property of its original creators
- No one else has permission to reproduce, distribute, or create derivative works
- Others cannot legally use, modify, or share the code without explicit permission

#### Recommendations
- Consider adding an open-source license to clarify usage terms
- Choose a license that aligns with your project's goals (e.g., MIT, Apache, GPL)
- Consult with legal counsel to understand the full implications of licensing

#### Current Status
Presently, no one is authorized to use this code without direct permission from the copyright holder.