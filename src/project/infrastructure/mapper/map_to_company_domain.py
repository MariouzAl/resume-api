from src.project.domain.entities.project_category import ProjectCategory
from src.project.infrastructure.models.project import Project as ProjectSQLModel
from src.project.domain.entities import Project


def map_to_project_domain(model: ProjectSQLModel) -> Project:
    return Project(
        id=model.id,
        project=model.project,
        shortDescription=model.shortDescription,
        link=model.link,
        projectLink=model.projectLink,
        categories=[
            ProjectCategory(id=category.id, name=category.name)
            for category in model.categories
        ]
        if model.categories is not None
        else [],
        builtWith=[skill.skill for skill in model.skills],
        images=[image.url for image in model.images],
        key=model.key,
        start_date=model.start_date,
        cover=model.cover,
        end_date=model.end_date,
        fullDescription=model.fullDescription,
        professional_experience_id=model.professional_experience_id
    )
