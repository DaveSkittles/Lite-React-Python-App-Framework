# Frontend

## TypeScript Setup

This project uses TypeScript 4.9.5, which is specifically chosen to be compatible with react-scripts 5.0.1. This version alignment is enforced through:

1. Explicit version in `devDependencies`: `"typescript": "4.9.5"`
2. Version resolution in `resolutions` field
3. Proper type definitions with `@types/react` and `@types/react-dom`

### Development

To check for TypeScript errors:

```bash
pnpm typecheck
```

### For New Contributors

When cloning the repository:

1. Use pnpm as the package manager:
   ```bash
   npm install -g pnpm
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

The correct TypeScript version will be automatically installed due to the version constraints in package.json.

### Version Compatibility

- TypeScript: 4.9.5 (compatible with react-scripts 5.0.1)
- React: ^18.3.1
- Node: >=14
- pnpm: >=7 